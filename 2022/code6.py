def main():
    file = open("input_6.txt", 'r')
    lines = file.readlines()
    line = lines[0]

    window = [line[0], line[1], line[2]]

    marker = 3

    for i in range(3, len(line)):
        marker += 1
        window.append(line[i])
        if len(set(window)) == len(window):
            break
        window.pop(0)

    print("Marker: ", marker)

    message_marker = []

    for i in range(0, 13):
        message_marker.append(line[i])

    marker = 13
    for i in range(13, len(line)):
        marker += 1
        message_marker.append(line[i])
        if len(set(message_marker)) == len(message_marker):
            break
        message_marker.pop(0)        

    print("Message Marker: ", marker)

if __name__ == '__main__':
    main()