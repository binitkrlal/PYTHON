# def generate_mirror_pattern(N, special_char):
#     # Generate the upper half of the pattern
#     pattern = ""
#     for i in range(N):
#         pattern += special_char * (i + 1) + "\n"

#     # Generate the lower half of the pattern (mirror reflection)
#     mirror_pattern = ""
#     for i in range(N - 1, -1, -1):
#         mirror_pattern += special_char * (i + 1) + "\n"

#     # Combine the upper and lower halves with a separator
#     combined_pattern = pattern + "|" + mirror_pattern 

#     return combined_pattern

# # Example usage:
# N = 5
# special_char = "*"
# result = generate_mirror_pattern(N, special_char)
# print(result)