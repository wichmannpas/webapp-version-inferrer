from backends.software_version import SoftwareVersion


class Guess:
    """
    A guess during analysis.
    """
    # software_version: SoftwareVersion
    # positive_matches: int

    def __init__(self, software_version: SoftwareVersion, positive_matches: int = 0):
        self.software_version = software_version
        self.positive_matches = positive_matches

    def __lt__(self, other) -> bool:
        return self.strength < other.strength

    def __le__(self, other) -> bool:
        return self.strength <= other.strength

    def __eq__(self, other) -> bool:
        return self.strength == other.strength

    def __ge__(self, other) -> bool:
        return self.strength >= other.strength
    
    def __gt__(self, other) -> bool:
        return self.strength > other.strength

    def __repr__(self) -> str:
        return "<{} '{}'>".format(str(self.__class__.__name__), str(self))

    def __str__(self) -> str:
        return '{} (+{})'.format(
            self.software_version,
            self.positive_matches)

    @property
    def strength(self) -> int:
        """The strength of the guess."""
        return self.positive_matches