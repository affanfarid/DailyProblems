
# Write a bash script to calculate the frequency of each word in a text file words.txt.

# For simplicity sake, you may assume:

#     words.txt contains only lowercase characters and space ' ' characters.
#     Each word must consist of lowercase characters only.
#     Words are separated by one or more whitespace characters.

# Example:

# Assume that words.txt has the following content:

# the day is sunny the the
# the sunny is is

# Your script should output the following, sorted by descending frequency:

# the 4
# is 3
# sunny 2
# day 1

allwords=()

# IFS=', ' read -r -a allwords <<< "$string"

input="words.txt"
while IFS= read -r line
do
  #echo "$line"
  IFS=', ' read -r -a allwords <<< "$line"
  
done < "$input"

for t in ${allwords[@]}; do
  echo $t
done

#echo Hello World

# for ((x=10; x>0; x-- ))
#   do
#   echo -n "$x "
# done
# printf "\n"

# file='words.txt'

# while IFS= read -r line
# do
#   echo $line
# done < $file



#example array. make sure no spaces around =
allThreads=()


for ((x=5; x>=0; x--)); do
  allThreads+=( $x )
done

for t in ${allThreads[@]}; do
  echo $t
done


