def normalize_name(inpt):
    work_in_progress = ''
    for i in inpt:
        if i.isalpha() or i == ' ':
            work_in_progress += i.lower()
    while not work_in_progress[0].isalpha():
        work_in_progress = work_in_progress[1:]
    while not work_in_progress[-1].isalpha():
        work_in_progress = work_in_progress[:-1]
    return_name = work_in_progress.replace(' ', '_')
    return return_name

def cumsum(numbers):
    for i in range(1, len(numbers)):
        numbers[i] += sum(numbers[i-1:i])
    return numbers