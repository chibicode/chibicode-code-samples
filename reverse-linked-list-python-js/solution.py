# Do not create a new dictionary
# Do not create a new list
# Do not add additional keys
def reverse_linked_list(linked_list):
    before = None
    current = linked_list
    while current:
        after = current["next"]
        current["next"] = before
        before = current
        current = after
    return before


if __name__ == "__main__":
    linked_list_1 = {"text": "A", "next": {"text": "B", "next": None}}

    linked_list_2 = {
        "text": "A",
        "next": {
            "text": "B",
            "next": {
                "text": "C",
                "next": {
                    "text": "D",
                    "next": None
                }
            }
        }
    }

    # {'text': 'B', 'next': {'text': 'A', 'next': None}}
    print(reverse_linked_list(linked_list_1))

    # {'text': 'D', 'next': {'text': 'C', 'next': {'text': 'B', 'next': {'text': 'A', 'next': None}}}}
    print(reverse_linked_list(linked_list_2))
