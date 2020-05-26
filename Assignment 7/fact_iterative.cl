(princ "Enter number whose factorial is to be found :   ")
(setq n (read))
(setq fact 1)
(loop for x from 1 to n
do (setq fact (* fact x)))
(princ "Factorial is :   ")
(princ fact)