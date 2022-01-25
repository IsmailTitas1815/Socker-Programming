import multiprocessing

square_result = []


def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square ' + str(n*n))
        square_result.append(n*n)
    print(square_result)


def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))


if __name__ == "__main__":
    arr = [2, 3, 8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("square_result:", square_result)

# if __name__ == '__main__':
#     port_input = random.randint(3000, 65000)

#     server = ServerSocket(port_input)
#     client = ClientSocket(port_input)

#     server_thread = multiprocessing.Process(
#         target=server.start_receiving, args=("server_file.csv", port_input))
#     client_thread = multiprocessing.Process(
#         target=client.sending_to_server, args=("client_file.csv", port_input))

#     server_thread.start()
#     client_thread.start()

#     server_thread.join()
#     client_thread.join()
