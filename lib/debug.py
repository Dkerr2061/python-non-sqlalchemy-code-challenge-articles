#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    magazine1 = Magazine('Vogue', 'Fashion')
    magazine2 = Magazine('Climbing Mag', 'Sports')
    magazine3 = Magazine('Surfing Magazine', 'Sports')

    author1 = Author('Bob')
    author2 = Author('Alice')
    author3 = Author('Dallas')

    article1 = Article(author1, magazine1, 'This is a random article about fashion')
    article2 = Article(author2, magazine2, "New news in the climbing world!")
    article3 = Article(author2, magazine3, "What's new in surfing!")
    article4 = Article(author3, magazine3, "Biggest wave ever!")
    article5 = Article(author3, magazine3, "Best starter spots in the world.")


    ipdb.set_trace()
