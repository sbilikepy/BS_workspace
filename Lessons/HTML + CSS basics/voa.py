def main(roster):
    msg = (f"/4 LFM VoA 25(19) spec run. Need: "
           f"{[i for i in roster if roster[i] is None]}. PM your gs or ilvl"
           ).replace("'", "").replace("[", "").replace(
        "]", ""
    )
    print(msg)
    return msg


if __name__ == "__main__":
    main(roster={
        "dk tank": None,
        "war tank": None,
        "pala tank": 1,
        "dru feral": 1,

        "pala holly": 1,
        "sham resto": 1,
        "dru resto": 1,
        "priest heal": 1,

        "sham enh": None,
        "sham elem": 1,
        "priest sp": None,
        "pala ret": 1,
        "dk dps": 1,
        "war dps": 1,
        "dru boom": 1,

        "warlock": 1,
        "mage": 1,
        "rogue": 1,
        "hunter": 1,

    })
