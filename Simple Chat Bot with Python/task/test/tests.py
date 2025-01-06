import re
from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

correct_feedback = ("Great job on completing Stage 1! You've successfully introduced your chat bot. As you progress "
                    "through the next stages, your bot will learn how to count and guess age. By the final stage, "
                    "you'll have an interactive quiz bot that can respond to you. Keep up the good work, and see how "
                    "your program evolves with each stage!")


class ChattyBotTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase()]

    def check(self, reply: str, clue: Any) -> CheckResult:
        lines = reply.strip().splitlines()
        if len(lines) != 2:
            return CheckResult.wrong(
                "You should output exactly 2 lines!\n" +
                f"Lines found: {len(lines)}"
                f"Your output:\n"
                f"{reply.strip()}"
            )

        if not re.match(".*\\d.*", lines[1]):
            return CheckResult.wrong(
                "The second line should contain a year!\n" +
                "Your second line: \"" + lines[1] + "\""
            )

        return CheckResult(True, correct_feedback)


if __name__ == '__main__':
    ChattyBotTest('bot.bot').run_tests()
