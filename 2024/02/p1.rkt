#lang racket

(provide solve
         safe?)

(require test-engine/racket-tests)

(define (solve reports)
  (count safe? reports))

;; safe?: (listof Int) -> Bool
(define (safe? report)
  (and (monotone? report) (andmap (lambda (d) (<= 1 (abs d) 3)) (differences report))))
(check-expect (safe? '(7 6 4 2 1)) #t)
(check-expect (safe? '(1 2 7 8 9)) #f)
(check-expect (safe? '(9 7 6 2 1)) #f)
(check-expect (safe? '(1 3 2 4 5)) #f)
(check-expect (safe? '(8 6 4 4 1)) #f)
(check-expect (safe? '(1 3 6 7 9)) #t)

(define (monotone? xs)
  (define diffs (differences xs))
  (or (andmap negative? diffs) (andmap positive? diffs)))
(check-expect (monotone? empty) #t)
(check-expect (monotone? '(1)) #t)
(check-expect (monotone? '(1 2 3 4)) #t)
(check-expect (monotone? '(1 0 0)) #f)
(check-expect (monotone? '(1 0 -1)) #t)

(define (differences xs)
  (map (lambda (ab) (- (first ab) (second ab))) (pairwise xs)))
(check-expect (differences empty) empty)
(check-expect (differences '(1)) empty)
(check-expect (differences '(4 3 3 1)) '(1 0 2))

;; pairwise: (listof Int) -> (listof (listof Int))
(define (pairwise xs)
  (cond
    [(empty? xs) empty]
    [(empty? (rest xs)) empty]
    [else (cons (list (first xs) (second xs)) (pairwise (rest xs)))]))
(check-expect (pairwise empty) empty)
(check-expect (pairwise '(1)) empty)
(check-expect (pairwise '(1 2)) '((1 2)))
(check-expect (pairwise '(1 2 3 4 5)) '((1 2) (2 3) (3 4) (4 5)))

(define (pairwise/fp xs)
  (define-struct state (acc prev))
  (cond
    [(empty? xs) empty]
    [else
     (reverse (state-acc (foldl (lambda (cur s)
                                  (define acc (state-acc s))
                                  (define prev (state-prev s))
                                  (make-state (cons (list prev cur) acc) cur))
                                (make-state empty (first xs))
                                (rest xs))))]))
(check-expect (pairwise/fp empty) empty)
(check-expect (pairwise/fp '(1)) empty)
(check-expect (pairwise/fp '(1 2)) '((1 2)))
(check-expect (pairwise/fp '(1 2 3 4 5)) '((1 2) (2 3) (3 4) (4 5)))
