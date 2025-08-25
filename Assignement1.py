{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1MohSzOYPw0ou7otTQrQa",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Saurav-gohill/Learnig-python/blob/main/Assignement1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X6SghVthvw29",
        "outputId": "2b10ede3-747a-4d9d-e66a-5691c2a3372d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "first number 98\n",
            "you operation what you want : +, -, *, /, //, %, **  *\n",
            "second number 78\n",
            "7644\n"
          ]
        }
      ],
      "source": [
        "# A simple Calculator\n",
        "a = int(input (\"first number \"))\n",
        "c = input(\"you operation what you want : +, -, *, /, //, %, **  \")\n",
        "b = int(input (\"second number \"))\n",
        "\n",
        "if c == '+':\n",
        "  print(a+b)\n",
        "elif c == '-':\n",
        "  print(a-b)\n",
        "elif c == '*':\n",
        "  print(a*b)\n",
        "elif c == '/':\n",
        "  print(a/b)\n",
        "elif c == '//':\n",
        "  print(a//b)\n",
        "elif c == '%':\n",
        "  print(a%b)\n",
        "elif c == '**':\n",
        "  print(a**b)\n",
        "else:\n",
        "  print(\"You enter wrong input\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Simple user credential\n",
        "user = 'admin'\n",
        "password = 'admin@123'\n",
        "\n",
        "user1 = input(\"Enter your user name  : \")\n",
        "passw = input(\"Enter your password to login  : \")\n",
        "\n",
        "if(user1 == user and passw == password):\n",
        "  print(\"login successful \")\n",
        "  print(\"welcome \", user1)\n",
        "elif(user1 == user):\n",
        "  print(\"user password is incorrect \")\n",
        "elif(passw == password):\n",
        "  print(\"Invalid user name\")\n",
        "else:\n",
        "  print(\"Invalid user name and passwod\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sb2OKlLV5Wjw",
        "outputId": "e9c0a699-e12d-4e4d-8312-1c564fc8336c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your user name  : admin\n",
            "Enter your password to login  : adminruhb\n",
            "user password is incorrect \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Print Grades\n",
        "name = input(\"Enter your name : \")\n",
        "marks = int(input(\"Enter your marks : \"))\n",
        "if marks >= 90:\n",
        "  print(name,\" your Grade is A+ \")\n",
        "elif marks >= 80:\n",
        "  print(name,\" your Grade is A \")\n",
        "elif marks >= 70:\n",
        "  print(name,\" your Grade is B \")\n",
        "elif marks >= 50:\n",
        "  print(name,\" your Grade is C \")\n",
        "else:\n",
        "  print(name,\" your Grade is D \")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u6T7r2LB70Y0",
        "outputId": "6cc04950-b820-4f68-e11b-aaee162936c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name : Bharti\n",
            "Enter your marks : 76\n",
            "Bharti  your Grade is B \n"
          ]
        }
      ]
    }
  ]
}