class PairFinder:
    @staticmethod
    def find_pairs(arr, target_sum):
        seen = {}  
        pairs = []  
        
        for num in arr:
            complement = target_sum - num
            if complement in seen:
                pairs.append((num, complement))
            seen[num] = True
        
        return pairs

def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python filename.py <comma-separated list of integers> <target integer>")
        return

    input_list = list(map(int, sys.argv[1].split(',')))
    target = int(sys.argv[2])

    pair_finder = PairFinder()
    result = pair_finder.find_pairs(input_list, target)

    for pair in result:
        print(pair[0], ",", pair[1])

if __name__ == '__main__':
    main()
