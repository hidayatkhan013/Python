# **Decoding a Secret Text Encrypted using a Cipher based on AES**

# Specification

## Aim

You are going to complete a Python 3 program so that it successfully decodes a secret message which is encoded using a baby block cipher related to AES.

## Blocks, Bytes and Nibbles

A block is 8 bits (or one byte, or one ASCII character). A key is 8 bits (or one byte). A block is treated as consisting of four nibbles, each nibble being two bits.

A block is 8 bits: 1 2 3 4 5 6 7 8.

Nibbles are: 1 2, 3 4, 5 6, 7 8.

A nibble can be treated either as two bits or as a number in arithmetic modulo 4 (that is, a number in the range 0−3).

## Elements of the Cipher

- Bitwise XOR of the block and the key;
- Replacing each nibble in a block by another nibble according to a substitution table (sometimes called an S-box);
- Swapping the last two nibbles of the block;
- Adding the last two nibbles to the first two nibbles, or subtracting the last two nibbles from the first two nibbles.

## Bitwise XOR

This is simply a bitwise XOR of the block and the key:

11101110

11010100

--------

00111010

## S-Box

When encrypting ( **FOR INFORMATION ONLY, WE ARE NOT DOING THIS**** )**, substitute the value of each nibble of the block as follows:

A value 0 becomes 1,

A value 1 becomes 3,

A value 2 becomes 0,

A value 3 becomes 2.

When decrypting ( **THIS IS WHAT WE ARE DOING**** )**, substitute the value of each nibble of the block in the opposite direction, as follows:

A value 0 becomes 2,

A value 1 becomes 0,

A value 2 becomes 3,

A value 3 becomes 1.

## Swapping Two Nibbles

Permute the positions of the last two nibbles of a block. In other words, a block

1 2, 3 4, 5 6, 7 8

becomes

1 2, 3 4, 7 8, 5 6

## Adding and Subtracting Nibbles

When encrypting ( **for information, we are not doing this** ), add the 3rd nibble to the 1st nibble and make that the new value of the 1st nibble; add the 4th nibble to the 2nd nibble and make that the new value of the 2nd nibble. The 3rd nibble and 4th nibble remain as they were before.

When decrypting ( **we are doing this** ), do the opposite: subtract the 3rd nibble from the 1st nibble and make that the new value of the 1st nibble; subtract the 4th nibble from the 2nd nibble and make that the new value of the 2nd nibble. The 3rd nibble and 4th nibble remain as they were before.

When doing addition and subtraction, treat each nibble as a number in arithmetic modulo 4 (that is, a number in the range 0−3). This is easy in Python even for negative numbers - see below.

## Encryption Algorithm (needs to be done)

- Bitwise XOR of the block and the key
- Use the S-box substitution on each nibble of the block
- Swap the last two nibbles of the block
- Add the last two nibbles to the first two
- Bitwise XOR of the block and the key
- Use the S-box substitution on each nibble of the block
- Swap the last two nibbles of the block
- Bitwise XOR of the block and the key

## Decryption algorithm (already done)

- Bitwise XOR of the block and the key

- Swap the last two nibbles of the block
- Use the S-box substitution on each nibble of the block
- Bitwise XOR of the block and the key
- Subtract the last two nibbles from the first two
- Swap the last two nibbles of the block
- Use the S-box substitution on each nibble of the block
- Bitwise XOR of the block and the key

## A Cipher to Decrypt

The following list of numbers is a text encrypted with the cipher:

[132, 201, 141, 74, 140, 94, 141, 140, 141, 15, 31, 164, 90, 229, 201, 141, 78, 114, 241, 217, 141, 217, 140, 180, 141, 164, 51, 141, 188, 221, 31,

164, 241, 177, 141, 140, 51, 217, 141, 201, 229, 152, 141, 78, 241, 114,

78, 102, 94, 141, 74, 152, 31, 152, 141, 94, 201, 31, 164, 102, 164, 51, 90, 141, 201, 229, 164, 31, 201, 152, 152, 51, 115]

The key used for encryption is 84.

Your task is to implement the decryption algorithm in Python and decrypt the cipher above. We also specify the encryption algorithm in case you would like to do that as well, for your own interest.

## Worked Example 1

Block 132 10 00 01 00

Key 84 01 01 01 00

XOR block and key 11 01 00 00

Swap last 2 nibbles 11 01 00 00

S-Box 01 00 10 10

Key 01 01 01 00

XOR Block &amp; Key 00 01 11 10

Subtract 2nd 2 from 1st 2 01 11 11 10

Swap last 2 nibbles 01 11 10 11

S-Box 00 01 11 01

Key 01 01 01 00

XOR Block &amp; Key 01 00 10 01

Answer: 73, i.e. &#39;I&#39;.

# How to Solve it

**First of all read all the instructions carefully, go through the worked example and make sure you understand it exactly! Then look at the program.**

The starting point is dec\_decrypt\_aes\_part.py. You are provided with this program. You can run this from the command line as follows:

python dec\_decrypt\_aes\_part.py a

python dec\_decrypt\_aes\_part.py b

python dec\_decrypt\_aes\_part.py c

python dec\_decrypt\_aes\_part.py d

python dec\_decrypt\_aes\_part.py e

Each argument causes a different function to be called:

a function dec\_decrypt applied to cipher text above (ie this checks your complete solution)

b function dec\_xor applied to two binary numbers in nibble form

c function dec\_swap\_last\_two applied to a binary number in nibble form

d function dec\_s\_box applied to a binary number in nibble form

e function dec\_subtract\_last\_two\_first\_two applied to a binary number in nibble form
