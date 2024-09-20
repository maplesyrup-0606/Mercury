def filter_no_padding(image, filter):
    f_size = len(filter)
    k = f_size // 2
    new_image = [[0 for i in range(len(image[0]))] for j in range(len(image))]

    for Y in range(k, len(image) - k):
        for X in range(k, len(image[Y]) - k):
            sum_ = 0
            for i in range(f_size):
                for j in range(f_size):
                    # print(image[Y - k + i][X - k + j], filter[i][j])
                    sum_ += image[Y - k + i][X - k + j] * filter[i][j]
            new_image[Y][X] = sum_

    print_matrix(new_image)
    return 0

def filter_zero_padding(image, filter):
    f_size = len(filter)
    k = f_size // 2
    img_pading = image.copy()
    img_pading.append([0 for i in range(len(image[0]) + 2 * k)])
    img_pading.insert(0, [0 for i in range(len(image[0]) + 2 * k)])
    for i in range(1, len(img_pading) - 1):
        img_pading[i] = [0] * k + img_pading[i] + [0] * k

    ret_img = img_pading.copy()

    for Y in range(k, len(image) - k):
        for X in range(k, len(image[Y]) - k):
            sum_ = 0
            for i in range(f_size):
                for j in range(f_size):
                    sum_ += img_pading[Y - k + i][X - k + j] * filter[i][j]
            ret_img[Y][X] = sum_

    print_matrix(ret_img)
    return 0


def print_matrix(matrix):
    for i in range(len(matrix)):
        str_ = ""
        for j in range(len(matrix[i])):
            str_ += str(matrix[i][j]) + " "
        if str_:
            print(str_)


def rotate_matrix_180(matrix):
    return [row[::-1] for row in matrix[::-1]]


def main():
    image = [[1, 0, 0, 0, 1], [2, 3, 0, 8, 0], [2, 0, 0, 0, 3], [0, 0, 1, 0, 0]]
    filter = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]

    # filter_no_padding(image, filter)

    # filter_no_padding(image, rotate_matrix_180(filter))

    padding_filter = [
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
    ]
    filter_zero_padding(image, padding_filter)


if __name__ == "__main__":
    main()
