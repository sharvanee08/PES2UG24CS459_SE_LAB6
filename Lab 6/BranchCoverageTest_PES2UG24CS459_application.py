
import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# BOOKING COST BRANCHES

@pytest.mark.parametrize("room,rate", [
    ("standard", 2000),
    ("deluxe", 3500),
    ("suite", 6000),
])
def test_room_rates(room, rate):
    assert booking_cost(room, 1, 2, False) == rate


def test_unknown_room():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("invalid", 1, 2, False)


def test_invalid_nights():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_peak_season():
    assert booking_cost("standard", 1, 2, True) == 2500


def test_non_peak_season():
    assert booking_cost("standard", 1, 2, False) == 2000


def test_extra_guests():
    assert booking_cost("standard", 2, 3, False) == 5000


def test_no_extra_guests():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_weekly_discount():
    assert booking_cost("standard", 7, 2, False) == 12600


def test_no_weekly_discount():
    assert booking_cost("standard", 6, 2, False) == 12000


# CANCELLATION REFUND BRANCHES

def test_refund_at_seven_days():
    assert cancellation_refund(1000, 7, False) == 1000


def test_refund_above_seven_days_member():
    assert cancellation_refund(1000, 10, True) == 1000


def test_refund_between_two_and_six_days():
    assert cancellation_refund(1000, 5, False) == 500


def test_member_refund_between_two_and_six_days():
    assert cancellation_refund(1000, 5, True) == 750


def test_refund_below_two_days():
    assert cancellation_refund(1000, 1, False) == 0


def test_member_refund_below_two_days():
    assert cancellation_refund(1000, 1, True) == 250


# ROOM UPGRADE BRANCHES

def test_no_rooms_available():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_upgrade():
    assert room_upgrade("standard", True, 1) == "deluxe"


def test_deluxe_member_upgrade():
    assert room_upgrade("deluxe", True, 1) == "suite"


def test_standard_nonmember():
    assert room_upgrade("standard", False, 1) == "standard"


def test_deluxe_nonmember():
    assert room_upgrade("deluxe", False, 1) == "deluxe"


def test_suite_member():
    assert room_upgrade("suite", True, 1) == "suite"
