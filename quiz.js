const questions = [
    {
        question: "What logical principle does a Stack data structure follow?",
        options: [
            "FIFO (First-In, First-Out)",
            "LIFO (Last-In, First-Out)",
            "LILO (Last-In, Last-Out)",
            "Random Access"
        ],
        answer: 1
    },
    {
        question: "Which operation is used to add an element to a Queue?",
        options: [
            "Push",
            "Pop",
            "Enqueue",
            "Dequeue"
        ],
        answer: 2
    },
    {
        question: "In a Circular Queue of size N, what is the formula to efficiently move the 'Rear' pointer to the next available position?",
        options: [
            "Rear = Rear + 1",
            "Rear = (Rear + 1) * N",
            "Rear = (Rear + 1) % N",
            "Rear = Rear % N"
        ],
        answer: 2
    },
    {
        question: "What state occurs when you attempt to remove an element from an empty Stack or Queue?",
        options: [
            "Overflow",
            "Underflow",
            "Memory Leak",
            "Deadlock"
        ],
        answer: 1
    },
    {
        question: "What is the primary advantage of a Circular Queue over a simple linear Queue?",
        options: [
            "It requires less memory allocation overall.",
            "It avoids wasting empty spaces at the front of the array caused by Dequeue operations.",
            "It allows fetching elements from both ends simultaneously.",
            "It automatically sorts the elements in a circular order."
        ],
        answer: 1
    }
];

let currentQuestionIndex = 0;
let score = 0;

const quizContainer = document.getElementById("quiz-container");
const resultContainer = document.getElementById("result-container");
const questionText = document.getElementById("question-text");
const optionsSection = document.getElementById("options");
const questionCountText = document.getElementById("question-count");
const scoreText = document.getElementById("score");
const nextBtn = document.getElementById("next-btn");
const finalScoreText = document.getElementById("final-score");
const resultMessageText = document.getElementById("result-message");
const restartBtn = document.getElementById("restart-btn");

function loadQuestion() {
    // Reset state
    nextBtn.classList.add("hidden");
    optionsSection.innerHTML = "";
    
    const currentQ = questions[currentQuestionIndex];
    questionText.textContent = currentQ.question;
    questionCountText.textContent = `Question ${currentQuestionIndex + 1} of ${questions.length}`;
    scoreText.textContent = `Score: ${score}`;
    
    currentQ.options.forEach((option, index) => {
        const btn = document.createElement("button");
        btn.className = "option-btn";
        btn.innerHTML = `<span>${option}</span><span class="option-icon"></span>`;
        btn.onclick = () => selectAnswer(index, btn);
        optionsSection.appendChild(btn);
    });
}

function selectAnswer(selectedIndex, selectedBtn) {
    // Disable all options
    const allOptions = optionsSection.querySelectorAll(".option-btn");
    allOptions.forEach(btn => btn.disabled = true);
    
    const currentQ = questions[currentQuestionIndex];
    
    if (selectedIndex === currentQ.answer) {
        selectedBtn.classList.add("correct");
        selectedBtn.querySelector(".option-icon").textContent = "✔️";
        score++;
        scoreText.textContent = `Score: ${score}`;
    } else {
        selectedBtn.classList.add("wrong");
        selectedBtn.querySelector(".option-icon").textContent = "❌";
        
        // Highlight correct answer
        allOptions[currentQ.answer].classList.add("correct");
        allOptions[currentQ.answer].querySelector(".option-icon").textContent = "✔️";
    }
    
    nextBtn.classList.remove("hidden");
}

nextBtn.addEventListener("click", () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        loadQuestion();
    } else {
        showResults();
    }
});

function showResults() {
    quizContainer.classList.add("hidden");
    resultContainer.classList.remove("hidden");
    
    finalScoreText.textContent = `${score}/${questions.length}`;
    
    let message = "";
    if (score === questions.length) {
        message = "Perfect score! You are a Data Structures master! 🏆";
    } else if (score >= 3) {
        message = "Great job! You have a solid grasp of Stacks & Queues! 👍";
    } else {
        message = "Keep learning! Give the theory boxes another read and try again! 📚";
    }
    resultMessageText.textContent = message;
}

restartBtn.addEventListener("click", () => {
    currentQuestionIndex = 0;
    score = 0;
    resultContainer.classList.add("hidden");
    quizContainer.classList.remove("hidden");
    loadQuestion();
});

// Initialize first question
document.addEventListener("DOMContentLoaded", () => {
    loadQuestion();
});
