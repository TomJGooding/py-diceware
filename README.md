# py-diceware

Diceware passphrase generator built with Python.

## Table of Contents

- [Usage](#usage)
  - [Number of Words](#number-of-words)
  - [Delimiter](#delimiter)
  - [Capitalisation](#capitalisation)
  - [Quiet Mode](#quiet-mode)

## Usage

Once installed, use `--help` to list all the available options:

```
$ py-diceware --help
Usage: py-diceware [OPTIONS]

  Diceware passphrase generator.

Options:
  -w, --words INTEGER RANGE  Number of words for passphrase.  [default: 6;
                             x>=1]
  -d, --delimiter TEXT       Delimiter to separate words in passphrase.
  --caps / --no-caps         Capitalise words in passphrase.  [default: caps]
  -q, --quiet                Only output the passphrase. Silence prompts and
                             other output.
  --help                     Show this message and exit.
```

### Number of Words

You can specify the number of words for the passphrase with the `-w` option:

```
$ py-diceware -w 8

#...

Your passphrase is:
UsdaChiveAlaskaWareTwSethShuckDeform
```

You will be prompted for the number of words if not provided from the command line:

```
$ py-diceware
Number of words [6]:

#...
```

The default number of words for the passphrase is 6, which is what is recommended for most users.

For more information about recommended passphrase lengths, refer to the ['How long should my passphrase be?'
section on the original Diceware FAQ](https://std.com/%7Ereinhold/dicewarefaq.html#howlong).

### Delimiter

By default the words in the passphrase will not be separated by any delimiter
(or more accurately, the default delimiter is just an empty string).

You can specify a delimiter for the passphrase with the `-d` option:

```
$ py-diceware -w 6 -d "_"

#...

Your passphrase is:
Spasm_Windy_Teet_Straw_Punish_Dj
```

The original Diceware method
[recommends separating each word with a space](https://std.com/~reinhold/dicewarefaq.html#spaces),
however this is not the default for py-diceware just based on the author's personal preference.
This also allows for quick copying of the passphrase with a double-click on Linux systems.

It could be argued that without any delimiter, the passphrase entropy is slightly reduced due to redundancy;
for example, the words "in put clammy" and "input clam my" would generate the same passphrase.
However, py-diceware mitigates this problem by capitalising each word by default
(see the [Capitalisation](#capitalisation) section below).

If you would prefer to generate a passphrase as recommended by the original Diceware method,
simply specify a space as the delimiter and no capitalisation of words:

```
$ py-diceware -w 6 -d " " --no-caps

#...

Your passphrase is:
flick aura junky meter alien throb
```

### Capitalisation

By default each word in the passphrase will be capitalised.

You can specify whether to capitalise words with the `-caps` or `--no-caps` option:

```
$ py-diceware -w 6 -d " " --no-caps

#...

Your passphrase is:
flick aura junky meter alien throb
```

All words in the Diceware list are lower case, and the original method
[does not recommend capitalising words](https://std.com/%7Ereinhold/dicewarefaq.html#capitalize)
as arguably this does make the passphrase slightly more difficult to type
(and harder to remember if characters are capitalised randomly, though this is not applicable for py-diceware).

However, the Diceware FAQ does note exceptions where some system password policies
"insist that you use a mix of uppercase and lower case letters"
or "where the length of the password is limited to 15 characters".

If you would prefer to generate a passphrase as recommended by the original Diceware method,
simply specify a space as the delimiter and no capitalisation of words like the example above.

It is recommended to use a delimiter if you choose not to capitalise the passphrase words,
otherwise this could slightly reduce the passphrase entropy as discussed above
in the [Delimiter](#delimiter) section.

### Quiet Mode

You can use the `--quiet` option to only output the passphrase and silence any prompts and other output:

```
$ py-diceware -w 8 -q
UsdaChiveAlaskaWareTwSethShuckDeform
```

If the number of words is not provided from the command line in quiet mode, the generated passphrase
will use the default of 6 words which is recommended for most users
(see the above [Number of Words](#number-of-words) section for more info).
