def count_bits(num):
    numBits = 0
    while num:
        numBits += num & 1
        num >>= 1
    return numBits

def main():
    print(count_bits(12))

if __name__ == "__main__":
    main()