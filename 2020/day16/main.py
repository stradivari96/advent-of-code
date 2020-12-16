from ortools.sat.python import cp_model


def parse(data):
    result = {
        "fields": {},
        "your ticket": [int(i) for i in data[1].split("\n")[1].split(",")],
        "tickets": [],
    }
    for field in data[0].split("\n"):
        k, v = field.split(": ")
        ranges = v.split(" or ")
        result["fields"][k] = [[int(i) for i in r.split("-")] for r in ranges]
    for ticket in data[2].split("\n")[1:]:
        result["tickets"].append([int(i) for i in ticket.split(",")])
    return result


def value_in_field(value, field):
    for r in field:
        if r[0] <= value <= r[1]:
            return True
    return False


def part_1(data):
    good_tickets = []
    result = 0
    for ticket in data["tickets"]:
        for n in ticket:
            if all(not value_in_field(n, f) for f in data["fields"].values()):
                result += n
                break
        else:
            good_tickets.append(ticket)
    print(result)
    return good_tickets


def part_2(data, good_tickets):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    column_field = {
        (i, j): model.NewBoolVar(f"{i}_{j}")
        for i in range(len(data["fields"]))
        for j in data["fields"]
    }
    for i in range(len(data["fields"])):
        model.Add(sum(column_field[i, j] for j in data["fields"]) == 1)
    for j in data["fields"]:
        model.Add(sum(column_field[i, j] for i in range(len(data["fields"]))) == 1)
    for ticket in good_tickets:
        for i, n in enumerate(ticket):
            for field, v in data["fields"].items():
                if not value_in_field(n, v):
                    model.Add(column_field[i, field] == 0)
    solver.Solve(model)
    columns = []
    for (i, j), v in column_field.items():
        if j.startswith("departure") and solver.Value(v):
            columns.append(i)
    result = 1
    for i in columns:
        result *= data["your ticket"][i]
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        data = parse(f.read().split("\n\n"))
    good_tickets = part_1(data)
    print(part_2(data, good_tickets))
