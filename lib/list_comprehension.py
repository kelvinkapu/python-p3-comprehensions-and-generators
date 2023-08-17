#!/usr/bin/env python3

def return_evens(num_list):
    return_evens = [num for num in num_list if num % 2 == 0]
    return return_evens


def make_exclamation(sentence_list):
    make_exclamation = [string + "!" for string in sentence_list]
    return make_exclamation