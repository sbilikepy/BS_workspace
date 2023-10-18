def main(roster):
    msg = (f"LFM VoA 25(19) spec run. Need: "
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
        "pala tank": None,
        "dru feral": None,

        "pala holly": None,
        "sham resto": None,
        "dru resto": None,
        "priest heal": None,

        "sham enh": None,
        "sham elem": None,
        "priest sp": None,
        "pala ret": None,
        "dk dps": None,
        "war dps": None,
        "dru boom": None,

        "warlock": 1,
        "mage": None,
        "rogue": None,
        "hunter": None,

    })
