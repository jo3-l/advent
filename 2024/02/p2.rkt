#lang racket

(provide solve)

(require test-engine/racket-tests)
(require "p1.rkt")

(define (solve reports)
  (count (lambda (r) (ormap safe? (dampen r))) reports))
(check-expect (solve '((7 6 4 2 1) (1 2 7 8 9) (9 7 6 2 1) (1 3 2 4 5) (8 6 4 4 1) (1 3 6 7 9))) 4)

(define (dampen lst)
  (cond
    [(empty? lst) empty]
    [else (cons (rest lst) (map (lambda (xs) (cons (first lst) xs)) (dampen (rest lst))))]))

(define (same-elements? xs ys <)
  (equal? (sort xs <) (sort ys <)))
(define (lex< xs ys)
  (cond
    [(empty? xs) (not (empty? ys))]
    [(empty? ys) #f]
    [(< (first xs) (first ys)) #t]
    [(= (first xs) (first ys)) (lex< (rest xs) (rest ys))]
    [else #f]))
(define (same-elements-as xs <)
  (lambda (ys) (same-elements? xs ys <)))

(check-satisfied (dampen '(1)) (same-elements-as '(()) lex<))
(check-satisfied (dampen '(1 2)) (same-elements-as '((1) (2)) lex<))
(check-satisfied (dampen '(1 2 3)) (same-elements-as '((2 3) (1 3) (1 2)) lex<))
