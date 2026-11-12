def vacuum_cleaner_agent(environment, start_location):
    """Simulates a Simple Reflex Vacuum Cleaner Agent."""
    location = start_location
    actions = []
    cost = 0

    for _ in range(len(environment) * 2):
        if all(status == "Clean" for status in environment.values()):
            break
        if environment[location] == "Dirty":
            actions.append(f"Location {location} is Dirty -> Action: SUCK")
            environment[location] = "Clean"
            cost += 1
        else:
            next_loc = "B" if location == "A" else "A"
            actions.append(f"Location {location} is Clean -> Action: MOVE to {next_loc}")
            location = next_loc
            cost += 1

    return actions, cost, environment

if __name__ == "__main__":
    steps, total_cost, final_env = vacuum_cleaner_agent({"A": "Dirty", "B": "Dirty"}, "A")
    for step in steps:
        print(step)
    print(f"Final Environment: {final_env} | Total Cost: {total_cost}")
