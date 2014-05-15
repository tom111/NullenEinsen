
barplot(table(rbinom (300,10,0.9)), width = 1, col = "red", border = par("fg"))

hist ( rbinom (300,10,0.9), col="red" , breaks=c(4.5, 5.5, 6.5,7.5,8.5,9.5,10.5), probability=TRUE) 
x <- seq(4.5, 10.5, .1) 
y <- dnorm(x,mean=9,sd= sqrt(.9)) 
lines(x,y)