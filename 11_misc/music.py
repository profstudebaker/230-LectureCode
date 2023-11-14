"""
Use these functions to write a chord progression
generator program. Feel free to take liberties with
the prompt. 

For each generated song idea, you should display 
a tempo, key, and a chord progression from that key. 

A user should be able to continue generating
song ideas until they decide to quit.  

BONUS: write a function that changes the position
of the chord to its musical notation in roman numerals. 
1 - 4 - 5 -> I - IV - V
"""
import random 

def get_tempo(min=60, max=180):
    """
    Randomly generates a tempo for a song
    within the given min and max values. Defaults are
    standard bounds for most songs.

    Params: 
    - min (optional) : integer
    - max (optional) : integer

    Returns:
    - integer 
    """
    return random.randint(min, max)

def get_key():
    """
    Randomly generates a key for a song
    from all of the possible major keys.

    Params: 
    - none

    Returns:
    - string (the name of the key)
    - position (the position in the array of the key, 
    used to pass in to the get_progression function)
    """
    KEYS = ['Ab','A','Bb','B','C','C#','Db','D','Eb','E','F','F#','Gb','G']
    key = random.choice(KEYS)
    position = KEYS.index(key)
    return key, position 

def get_progression(key_position, n_chords=4):
    """
    Randomly generates a chord progression for the given key.
    Default number of chords in progression is 4. 

    Params:
    - key_position : integer
    (the position of the key, used to select possible chords in that key)
    - n_chords (optional) : integer
    (number of chords to generate in the progression)

    Returns:
    - string of the names of the chords in the progression
    """
    CHORDS = [
        "Ab	Bbm	Cm	Db	Eb	Fm	Gdim",
        "A	Bm	C#m	D	E	F#m	G#dim",
        "Bb	Cm	Dm	Eb	F	Gm	Adim",
        "B	C#m	D#m	E	F#	G#m	A#dim",
        "C	Dm	Em	F	G	Am	Bdim",
        "C#	D#m	E#m	F#	G#	A#m	B#dim",
        "Db	Ebm	Fm	Gb	Ab	Bbm	Cdim",
        "D	Em	F#m	G	A	Bm	C#dim",
        "Eb	Fm	Gm	Ab	Bb	Cm	Ddim",
        "E	F#m	G#m	A	B	C#m	D#dim",
        "F	Gm	Am	Bb	C	Dm	Edim",
        "F#	G#m	A#m	B	C#	D#m	E#dim",
        "Gb	Abm	Bbm	Cb	Db	Ebm	Fdim",
        "G	Am	Bm	C	D	Em	F#dim",
    ]
    chords_in_key = CHORDS[key_position].split()
    chords = []
    for i in range(n_chords):
        chords.append(random.choice(chords_in_key))
    return ' '.join(chords)


if __name__ == "__main__":
    print(get_tempo(50, 70))
    # key = get_key()
    # key_name = key[0]
    # key_pos = key[1]
    key_name, key_pos = get_key()
    print(key_name, key_pos)
    print(get_progression(0))
