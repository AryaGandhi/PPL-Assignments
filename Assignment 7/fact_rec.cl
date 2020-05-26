(princ "Enter the number whose factorial is to be found :   ")
(defun fact(n)
    (if (= n 0) 1
        (* n (fact(- n 1)))
    )
)

(setq n (read))
(setq f (fact n))
(princ "Factorial is :   ")
(princ f)