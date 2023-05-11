def main():
    names = ['Bill', 'John', 'Kurt']
    scores = [100, 90, 90]

    for zobj in zip(names, scores):
        print(zobj)

    return zip(names, scores)


if __name__ == '__main__':
    main()
