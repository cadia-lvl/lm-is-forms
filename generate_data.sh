mkdir -p data
export n=100000
python3 generate_data.py phone_number $n | python3 normalize_numbers.py phone_number - > data/phone_numbers_normalized.txt
python3 generate_data.py kennitala $n | python3 normalize_numbers.py kennitala - > data/kennitalas_normalized.txt
