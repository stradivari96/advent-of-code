if __name__ == "__main__":
    with open("data.txt") as f:
        boarding_passes = f.read()
    boarding_passes = boarding_passes.split("\n")

    seat_ids = set()
    for boarding_pass in boarding_passes:
        low, high = 0, 127
        for half in boarding_pass[:7]:
            mid = (high + low) // 2
            if half == "F":
                high = mid
            else:
                low = mid + 1
        row = low
        low, high = 0, 7
        for half in boarding_pass[-3:]:
            mid = (high + low) // 2
            if half == "L":
                high = mid
            else:
                low = mid + 1
        column = low
        seat_ids.add(row * 8 + column)
    print(max(seat_ids))

    for seat_id in seat_ids:
        if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
            print(seat_id + 1)
            break
