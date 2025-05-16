const questions = [
  {
    question: "What is the capital of France?",
    options: ["Berlin", "Paris", "Madrid", "Rome"],
    answer: 1
  },
  {
    question: "Which planet is known as the Red Planet?",
    options: ["Earth", "Venus", "Mars", "Jupiter"],
    answer: 2
  },
  {
    question: "What is the chemical symbol for water?",
    options: ["H2O", "O2", "CO2", "H2"],
    answer: 0
  }
];

let currentQuestion = 0;
let score = 0;

const startScreen = document.getElementById("start-screen");
const quizScreen = document.getElementById("quiz-screen");
const resultScreen = document.getElementById("result-screen");
const questionBox = document.getElementById("question-box");
const optionsBox = document.getElementById("options-box");
const nextBtn = document.getElementById("next-btn");
const scoreText = document.getElementById("score-text");

function startQuiz() {
  startScreen.classList.add("hide");
  quizScreen.classList.remove("hide");
  shuffleQuestions();
  showQuestion();
}

function shuffleQuestions() {
  questions.sort(() => Math.random() - 0.5);
  questions.forEach(q => {
    q.options = q.options.map((opt, i) => ({ text: opt, index: i }))
                         .sort(() => Math.random() - 0.5);
  });
}

function showQuestion() {
  nextBtn.classList.add("hide");
  const q = questions[currentQuestion];
  questionBox.textContent = q.question;
  optionsBox.innerHTML = "";

  q.options.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.textContent = opt.text;
    btn.className = "option";
    btn.onclick = () => selectAnswer(opt.index);
    optionsBox.appendChild(btn);
  });
}

function selectAnswer(selected) {
  const correctIndex = questions[currentQuestion].answer;
  const options = optionsBox.querySelectorAll(".option");

  options.forEach((btn, i) => {
    const isCorrect = questions[currentQuestion].options[i].index === correctIndex;
    btn.style.background = isCorrect ? "lightgreen" : "lightcoral";
    btn.disabled = true;
  });

  if (selected === correctIndex) score++;

  nextBtn.classList.remove("hide");
}

function nextQuestion() {
  currentQuestion++;
  if (currentQuestion < questions.length) {
    showQuestion();
  } else {
    showResult();
  }
}

function showResult() {
  quizScreen.classList.add("hide");
  resultScreen.classList.remove("hide");
  scoreText.textContent = `You scored ${score} out of ${questions.length}`;
}
