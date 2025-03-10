if __name__ == '__main__':
    student_list = []  # Step 1: Initialize list

    for i in range(int(input())):  # Step 1: Read input
        name = input()
        score = float(input())
        student_list.append([name, score])
    
    unique_scores = sorted(set([score for name,score in student_list]))
    second_lowest = unique_scores[1]
    names = sorted([name for name,score in student_list if score==second_lowest])#lexicographical order
    print('\n'.join(names))