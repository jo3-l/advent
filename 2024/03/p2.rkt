#lang racket

(provide solve)

(require test-engine/racket-tests)

(define (solve prog)
  (define-struct state (enabled? acc))
  (define products
    (state-acc (foldl (lambda (m s)
                        (define enabled? (state-enabled? s))
                        (define acc (state-acc s))
                        (cond
                          [(string=? (first m) "do()") (make-state #t acc)]
                          [(string=? (first m) "don't()") (make-state #f acc)]
                          [enabled?
                           (define x (string->number (second m)))
                           (define y (string->number (third m)))
                           (make-state #t (cons (* x y) acc))]
                          [else (make-state #f acc)]))
                      (make-state #t empty)
                      (regexp-match* #px"do\\(\\)|don't\\(\\)|mul\\((\\d{1,3}),(\\d{1,3})\\)"
                                     prog
                                     #:match-select values))))
  (foldr + 0 products))

(check-expect (solve "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") 48)
