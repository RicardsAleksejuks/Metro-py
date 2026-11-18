from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


@app.route("/alkuluku/<int(signed=True):number>", methods=["GET"])
def check_prime(number: int):
    return jsonify({"Number": number, "isPrime": is_prime(number)})


if __name__ == "__main__":
    app.run(port=3000)