setwd("D:/project/xcourse/sentiment")
script <- read.csv("shss.csv", stringsAsFactors=FALSE)

library(dplyr)
library(tidytext)
library(tidyr)
library(ggplot2)

#split the script into words 
tidy_script <- unnest_tokens(script, word, text)
#analyze the sentiments of each word
sentiment_each_word <- inner_join(tidy_script, get_sentiments("nrc")) 
#get the number of the sentiments
sentiment_count <- count(sentiment_each_word, sentiment)