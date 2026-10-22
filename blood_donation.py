"""Manage blood donors, donations, and blood stock."""
import os
import tempfile
from datetime import date, timedelta


donors = []
stock = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "O+": 0,
    "O-": 0,
    "AB+": 0,
    "AB-": 0,
}
COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
}


def register_donor(donor_name, blood_group, age, last_donation=None,
                   notes=None):
    """Register an eligible donor and record any age-related rejection."""
    if notes is None:
        notes = []

    if blood_group not in stock:
        raise ValueError("Unknown blood group")

    if age < 18 or age > 65:
        notes.append(f"{donor_name} is not eligible because of age")
        return False

    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Check whether a donor is eligible to donate again."""
    if donor["last"] is None:
        return True
    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation if the donor is eligible."""
    for donor in donors:
        if donor["name"] == donor_name and can_donate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Return the available units compatible with a patient's blood group."""
    try:
        return sum(stock[group] for group in COMPATIBLE[patient_group])
    except KeyError:
        return 0


def is_universal(blood_group):
    """Check whether a blood group is a universal donor or recipient."""
    return blood_group in {"O-", "AB+"}


def low_stock(threshold=2):
    """Return blood groups whose stock is below the threshold."""
    return [
        group
        for group, units in stock.items()
        if units < threshold
    ]


def donor_sheet_path():
    """Create and return a secure temporary CSV file path."""
    file_descriptor, file_path = tempfile.mkstemp(
        suffix=".csv")
    os.close(file_descriptor)
    return file_path


def notify_donors(phone_list):
    """Validate and return phone numbers for future notifications."""
    if not all(isinstance(phone, str) and phone.strip()
               for phone in phone_list):
        raise ValueError("Phone numbers must be non-empty strings")
    return list(phone_list)


def main():
    """Demonstrate donor registration and blood stock management."""
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)

    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")

    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    # Display blood groups with fewer than two units.
    print("Low stock groups:", low_stock())

    eligible = [
        donor["name"]
        for donor in donors
        if can_donate(donor)
    ]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
