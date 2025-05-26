document.addEventListener('DOMContentLoaded', function () {
  const button = document.querySelector('.signin-button');

  button.addEventListener('click', function () {
    const username = document.querySelector('input[placeholder="Username"]').value;
    const studentNum = document.querySelector('input[placeholder="Student number"]').value;
    const phone = document.querySelector('input[placeholder="Phone number"]').value;

    // 👉 로그인 조건 예시
    if (username === 'admin' && studentNum === '1234' && phone === '010-0000-0000') {
      window.location.href = 'main.html'; // ✅ 성공 시 페이지 이동
    } else {
      alert('로그인에 실패했습니다. 다시 시도해주세요.'); // ❌ 실패 시 알림
    }
  });
});