class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
    let stackPosSpeed = position
        .map((x, index) => ({
            position: x, 
            speed: speed[index]
        }))
        .sort((a, b) => a.position - b.position);

    console.log(stackPosSpeed);

    if (stackPosSpeed.length == 1) return 1;

    let next = stackPosSpeed.pop();
    let counter = position.length;

    while (stackPosSpeed.length !== 0) {
        const current = stackPosSpeed.pop()
        const a = next.speed;
        const b = next.position;
        const c = current.speed;
        const d = current.position;

        console.log("next speed ", a, " next pos ",b, " curr speed ",c, " curr pos ",d);

        const meeting = a * (d - b) / (a - c) + b;
        console.log(meeting);

        if (target >= meeting && c > a) {
            counter--;
            current.speed = next.speed;
            current.position = next.position;
        }

        next = current;
    }

    return counter;
    }
}
