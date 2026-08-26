#!/bin/bash
fruits=("Apple" "Banana" "Avocado" "Pineapple" "Mango")
echo "Item 1: ${fruits[0]}"
echo "Item 2: ${fruits[1]}"
echo "Item 3: ${fruits[2]}"
echo "Item 4: ${fruits[3]}"
echo "Item 5: ${fruits[4]}"

echo "Total fruits: ${#fruits[@]}"