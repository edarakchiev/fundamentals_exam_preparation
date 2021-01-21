def piece_check(pieces_dict, piece_to_check):
    if piece_to_check in pieces_dict:
        return True
    return False


n = int(input())
pieces = {}
for _ in range(n):
    add_piece, add_composer, add_key = input().split("|")
    pieces[add_piece] = {"composer": add_composer, "key_txt": add_key}

while True:
    data = input()
    if data == "Stop":
        break
    data = data.split("|")
    command = data[0]
    piece = data[1]
    if command == "Add":
        composer = data[2]
        key_txt = data[3]
        if piece_check(pieces, piece):
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key_txt": key_txt}
            print(f"{piece} by {composer} in {key_txt} added to the collection!")
    elif command == "Remove":
        if piece_check(pieces, piece):
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = data[2]
        if piece_check(pieces, piece):
            pieces[piece]['key_txt'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))
for key_piece, value_piece in sorted_pieces:
    print(f"{key_piece} -> Composer: {value_piece['composer']}, Key: {value_piece['key_txt']}")
