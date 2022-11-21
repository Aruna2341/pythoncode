import pexpect
child=pexpect.spawn("echo myworld")

print(child.expect(["hello", "welcome", "myworld"]))