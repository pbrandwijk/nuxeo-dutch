
print("Analyzing translation files...");

file_en = open('../messages.properties');
file_nl = open('../messages_nl.properties');

tokens_en = [];
translations_en = {}
dict_nl = {};

# Open target file
file = open('../messages_nl.properties-reordered', 'w+');

# First we'll inspect each line to see if it contains a translation, an empty line or a comment
for line in file_en:
	if "=" in line:
		# If it contains a translation, add the token to our little list and save the translation to our dictionary of English tokens -> translations
		tokens_en.append(line.split("=")[0].strip());
		translations_en[line.split("=")[0].strip()] = line.split("=")[1].strip()
	elif not line.strip():
		tokens_en.append("[EMPTYLINE]");
	elif "#" in line:
		tokens_en.append(line);

# Create a dictionary for Dutch tokens -> translations
for line in file_nl:
	if "=" in line:
		dict_nl[line.split("=")[0].strip()] = line;

# Now rebuild the English file, using the Dutch translations.
for t in tokens_en:
	print(t);
	if t is "[EMPTYLINE]":
		file.write("\n");
	elif "#" in t:
		file.write(t);
	elif t in dict_nl.keys():
		file.write(dict_nl[t]);
	else:
		# Specify if a translation is missing
		file.write(t + "=<MISSING TRANSLATION: " + translations_en[t] + ">\n");

file_en.close();
file_nl.close();
file.close();