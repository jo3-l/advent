#lang racket

(require (rename-in "p1.rkt" (solve solve/part1)))
(require (rename-in "p2.rkt" (solve/hashed solve/part2)))

(define rows
  (file->list "input.txt"
              (lambda (in)
                (define x (read in))
                (define y (read in))
                (if (eof-object? x) eof (list x y)))))

(define (parse xs ys rows)
  (cond
    [(empty? rows) (values (reverse xs) (reverse ys))]
    [else
     (define r (first rows))
     (parse (cons (first r) xs) (cons (second r) ys) (rest rows))]))

(define-values (xs ys) (parse empty empty rows))
(printf "part 1: ~a\n" (solve/part1 xs ys))
(printf "part 2: ~a\n" (solve/part2 xs ys))
