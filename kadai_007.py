{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "# リストの作成\n",
        "array = [\n",
        "    \"月曜日は晴れです\",\n",
        "    \"火曜日は雨です\",\n",
        "    \"水曜日は晴れです\",\n",
        "    \"木曜日は晴れです\",\n",
        "    \"金曜日は曇りです\",\n",
        "    \"土曜日は曇りのち雨です\",\n",
        "    \"日曜日は雷雨です\",\n",
        "]\n",
        "\n",
        "# リストから水曜日の天気を取り出して出力\n",
        "print(array[2])  # \"水曜日は晴れです\"\n",
        "\n",
        "# ディクショナリの作成\n",
        "dictionary = {\n",
        "    \"mon\": \"晴れ\",\n",
        "    \"tue\": \"雨\",\n",
        "    \"wed\": \"晴れ\",\n",
        "    \"thu\": \"晴れ\",\n",
        "    \"fri\": \"曇り\",\n",
        "    \"sat\": \"曇りのち雨\",\n",
        "    \"sun\": \"雷雨\",\n",
        "}\n",
        "\n",
        "# ディクショナリから水曜日の天気を取り出して出力\n",
        "print(f\"水曜日の天気は{dictionary['wed']}です\")  # \"水曜日の天気は晴れです\"\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PRLeT8Xdu65k",
        "outputId": "e5e087e0-7352-4668-c360-89c9c920be87"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "水曜日は晴れです\n",
            "水曜日の天気は晴れです\n"
          ]
        }
      ]
    }
  ]
}