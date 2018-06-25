# *** MERGING MEETING TIMES ***
#Write a function merge_ranges() that takes a list of multiple meeting time 
#ranges and returns a list of condensed ranges.

def merge_ranges(meetings):
    
    # sort list of tuples
    meetings_sorted = sorted(meetings)

    # create new list
    merged_meetings = [meetings_sorted[0]]

    # iterate through list and unpack tuples
    for current_start, current_end in meetings_sorted:
        merged_start, merged_end = merged_meetings[-1]

        if current_start <= merged_end:
            merged_meetings[-1] = (merged_start, max(merged_end, current_end))

        else:
            merged_meetings.append((current_start, current_end))

    return merged_meetings

# O(nlgn) time and O(n)O(n) space.

################################################################################
# *** REVERSE STRING IN PLACE ***
# Write a function that takes a list of characters and reverses the letters in-place

# swap lst[i] with lst[-i -1]
# swap lst[0] with lst[-0-1 = -1]
# swap lst[1] with lst[-1-1 = -2]

def reverse_list(lst):

    # counter
    i = 0

    # swap up to midpoint
    midpoint = len(lst)/2

    # iterate through list
    for item in range(midpoint):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp

        i += 1

    return lst

# Runtime: O(n), space O(1)

  def reverse_characters(message):
    left_index = 0
    right_index = len(message) - 1

    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1

################################################################################
# *** REVERSE WORDS ***
# Write a function reverse_words() that takes a message as a list of characters 
# and reverses the order of the words in-place

# create helper function to reverse entire list
# iterate through reversed list
# find seperate words through ' '
# if index is len(lst) or lst[index] is ' '
    # reverse characters 
def reverse_words(lst):


    # iterate through the list to reverse characters
    def reverse_characters(lst, left_index, right_index):

        while left_index < right_index:
            lst[left_index], lst[right_index] = lst[right_index], lst[left_index]
            left_index += 1
            right_index -= 1

    # use helper function to reverse list
    reverse_characters(lst, 0, len(lst)-1)

    current_index = 0

    for i in range(len(lst) + 1):
        if i == len(lst) or lst[i] == ' ':
            reverse_characters(lst, current_index, i-1)
            current_index = i + 1

    print ''.join(lst)

# ['l', 'a', 'e', 't', 's', ' ', 'd', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c']
# 0
# 1
# 2
# 3
# 4
# 5

# lst, current index, i-1 ['s', 't', 'e', 'a', 'l', ' ', 'd', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c'] 0 4
# current index 6
# 6
# 7
# 8
# 9
# 10
# 11

# lst, current index, i-1 ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'e', 'k', 'a', 'c'] 6 10
# current index 12
# 12
# 13
# 14
# 15
# 16

# lst, current index, i-1 ['s', 't', 'e', 'a', 'l', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e'] 12 15
# current index 17

################################################################################
# *** MERGE SORTED ARRAYS *** 
# Write a function to merge our lists of orders into one sorted list.

# create new list
# compare the two list:
# i = 0

# while len(my_item(i)) <= len(alice_item[i])

    # if my_item < alice_item:
        # add my item to new list
        # add alice's item to list
    # else:
        # add alice's item
        # add my item 
    # i += 1

# list.extend(my_list[i:])
# list.extend(alice_list[i:])

# return lst

def merge_sort(lst1, lst2):

    merged = []
    i = 0

    while len(lst1) <= len(lst2) and i < len(lst1):
        print i
        if lst1[i] < lst2[i]:
            merged.append(lst1[i])
            merged.append(lst2[i])
        else:
            merged.append(lst2[i])
            merged.append(lst1[i])
        i += 1

    merged.extend(lst1[i:])
    merged.extend(lst2[i:])

    return merged

# keep track of length of combined list
# create new list (merged_list)
# lst1_index
# lst2_index
# current_merged_index

# while current_merged_index < merge_list_size
    # check to see if current index < len of lists
    # lst1_exhausted = lst1_index >= len(lst1)
    # lst2_exhausted = lst2_index >= len(lst2)

    # if lst1 not exhausted and (lst2 IS exhausted or lst1[lst1_i] < lst2[lst2_i])
        # merged_list[current_merged_i] = lst1[lst1_i]
        # lst1_i += 1

    # else
        # merge_list[current_merged_i] = lst2[lst2_i]
        # lst2_i += 1

# return merged_list

def merge_lists(lst1, lst2):
    list_size = len(lst1) + len(lst2)
    merged_list = [None] * list_size

    lst1_i = 0
    lst2_i = 0
    merged_current_i = 0

    while merged_current_i < list_size:
        is_lst1_exhausted = lst1_i >= len(lst1)
        is_lst2_exhausted = lst2_i >= len(lst2)

        if not is_lst1_exhausted and (is_lst2_exhausted or lst1[lst1_i] < lst2[lst2_i]):
            merged_list[merged_current_i] = lst1[lst1_i]
            lst1_i += 1
        else:
            merged_list[merged_current_i] = lst2[lst2_i]
            lst2_i += 1

        merged_current_i += 1

    return merged_list

################################################################################
# *** SINGLE RIFFLE SHUFFLE
# let's write a function to tell us if a full deck of cards shuffled_deck is a 
# single riffle of two other halves half1 and half2.

# RECURSIVELY
def is_single_riffle(half1, half2, shuffled_deck):
    # base case
    if len(shuffled_deck) == 0:
        return True

    # if top of shuffled_deck is same as top of half1
    if len(half1) and half1[0] == shuffled_deck[0]:
        # remove top card off half1 & shuffled deck
        return is_single_riffle(half1[1:], half2, shuffled_deck[1:])

    # if top of shuffled_deck is same as top of half2
    elif len(half2) and half2[0] == shuffled_deck[0]:
        # remove top card off half2 & shuffled deck
        return is_single_riffle(half1, half2[1:], shuffled_deck[1:])

    # top card doesn't match top half1 or half2, not single riffle
    else:
        return False
# O(n) time & O(n) space

# ITERATIVELY 
def is_single_riffle2(half1, half2, shuffled_deck):
    half1_i = 0
    half2_i = 0
    half1_max = len(half1) - 1
    half2_max = len(half2) - 1

    for card in shuffled_deck:
        if half1_i <= half1_max and card == half1[half1_i]:
            half1_i += 1

        elif half2_i <= half2_max and card == half2[half2_i]:
            half2_i += 1

        else:
            return False

    # all cards have been checked
    return True

# O(n) time & O(1) space

################################################################################
# *** REVERSE A LINKED LIST ***
# Write a function for reversing a linked list. ↴ Do it in-place. 

class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse_linked_list(head):
    # identify current, previous, next
    current = head
    previous = None
    next = None

    while current:
        # copy pointer to next element
        next = current.next

        # reverse next pointer
        current.next = previous

        # step forward in list
        previous = current
        current = next

    return previous

# 1-2-3-4

# c = 1
# p = None
# n = None

# while head exists:
#     next = 2
#     current.next = (previous) None

#     previous = 1
#     current = 2
#     ----
#     next = 3
#     current.next = 1

#     previous = 2
#     current = 3
#     ----
#     next = 4
#     current.next = 2

#     previous = 3
#     current = 4
#     ----
#     next = None
#     current.next = 3

#     previous = 4
#     current = None

# return previous 
