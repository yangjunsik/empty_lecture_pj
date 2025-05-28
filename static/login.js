// 로그인 페이지 전용 JavaScript
document.addEventListener('DOMContentLoaded', function() {
  const loginForm = document.querySelector('.login-form');
  const loginBtn = document.getElementById('loginBtn');
  const loginText = document.getElementById('loginText');
  const loginSpinner = document.getElementById('loginSpinner');

  // 입력 필드들
  const studentIdInput = document.getElementById('student_id');
  const nameInput = document.getElementById('name');
  const phoneInput = document.getElementById('phone');

  // 폼 제출 시 로딩 상태 표시
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      // 기본 유효성 검사
      if (!validateForm()) {
        e.preventDefault();
        return;
      }

      // 로딩 상태 시작
      setLoading(true);
    });
  }

  // 전화번호 자동 포맷팅
  if (phoneInput) {
    phoneInput.addEventListener('input', function(e) {
      let value = e.target.value.replace(/[^\d]/g, ''); // 숫자만 추출

      if (value.length >= 3 && value.length <= 7) {
        value = value.replace(/(\d{3})(\d{1,4})/, '$1-$2');
      } else if (value.length >= 8) {
        value = value.replace(/(\d{3})(\d{4})(\d{1,4})/, '$1-$2-$3');
      }

      e.target.value = value;
    });

    // 전화번호 입력 시 최대 길이 제한
    phoneInput.addEventListener('keypress', function(e) {
      const value = e.target.value.replace(/[^\d]/g, '');
      if (value.length >= 11 && e.key !== 'Backspace' && e.key !== 'Delete') {
        e.preventDefault();
      }
    });
  }

  // 학번 입력 시 숫자만 허용
  if (studentIdInput) {
    studentIdInput.addEventListener('input', function(e) {
      // 숫자만 허용
      e.target.value = e.target.value.replace(/[^\d]/g, '');
    });
  }

  // 이름 입력 시 한글과 영문만 허용
  if (nameInput) {
    nameInput.addEventListener('input', function(e) {
      // 한글, 영문, 공백만 허용
      e.target.value = e.target.value.replace(/[^가-힣a-zA-Z\s]/g, '');
    });
  }

  // Enter 키로 다음 필드로 이동
  studentIdInput?.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      nameInput?.focus();
    }
  });

  nameInput?.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      phoneInput?.focus();
    }
  });

  phoneInput?.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      if (validateForm()) {
        loginForm?.submit();
      }
    }
  });

  // 폼 유효성 검사
  function validateForm() {
    const studentId = studentIdInput?.value.trim();
    const name = nameInput?.value.trim();
    const phone = phoneInput?.value.trim();

    // 학번 검사 (8자리 숫자)
    if (!studentId || studentId.length < 6) {
      showFieldError(studentIdInput, '학번을 정확히 입력해주세요.');
      return false;
    }

    // 이름 검사 (2글자 이상)
    if (!name || name.length < 2) {
      showFieldError(nameInput, '이름을 정확히 입력해주세요.');
      return false;
    }

    // 전화번호 검사 (010-0000-0000 형식)
    const phoneRegex = /^010-\d{4}-\d{4}$/;
    if (!phone || !phoneRegex.test(phone)) {
      showFieldError(phoneInput, '전화번호를 010-0000-0000 형식으로 입력해주세요.');
      return false;
    }

    // 모든 에러 메시지 제거
    clearFieldErrors();
    return true;
  }

  // 필드별 에러 표시
  function showFieldError(field, message) {
    clearFieldErrors();

    field.style.borderColor = '#ef4444';
    field.style.backgroundColor = '#fef2f2';

    // 에러 메시지 요소 생성
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.textContent = message;
    errorDiv.style.cssText = `
            color: #ef4444;
            font-size: 12px;
            margin-top: 4px;
            font-weight: 500;
        `;

    field.parentNode.appendChild(errorDiv);
    field.focus();
  }

  // 필드 에러 제거
  function clearFieldErrors() {
    // 기존 에러 메시지 제거
    document.querySelectorAll('.field-error').forEach(error => {
      error.remove();
    });

    // 필드 스타일 초기화
    [studentIdInput, nameInput, phoneInput].forEach(field => {
      if (field) {
        field.style.borderColor = '';
        field.style.backgroundColor = '';
      }
    });
  }

  // 로딩 상태 설정
  function setLoading(loading) {
    if (loading) {
      loginBtn.disabled = true;
      loginText.textContent = '로그인 중...';
      loginSpinner.style.display = 'inline-block';
    } else {
      loginBtn.disabled = false;
      loginText.textContent = '로그인';
      loginSpinner.style.display = 'none';
    }
  }

  // 입력 필드 포커스 시 에러 상태 제거
  [studentIdInput, nameInput, phoneInput].forEach(field => {
    if (field) {
      field.addEventListener('focus', function() {
        this.style.borderColor = '#667eea';
        this.style.backgroundColor = 'white';

        // 해당 필드의 에러 메시지만 제거
        const errorMsg = this.parentNode.querySelector('.field-error');
        if (errorMsg) {
          errorMsg.remove();
        }
      });
    }
  });

  // 페이지 로드 시 첫 번째 필드에 포커스
  if (studentIdInput) {
    studentIdInput.focus();
  }
});

// 유틸리티 함수들
function formatPhoneNumber(phone) {
  const cleaned = phone.replace(/\D/g, '');
  const match = cleaned.match(/^(\d{3})(\d{4})(\d{4})$/);
  if (match) {
    return `${match[1]}-${match[2]}-${match[3]}`;
  }
  return phone;
}

function validateStudentId(studentId) {
  return /^\d{6,10}$/.test(studentId);
}

function validateName(name) {
  return /^[가-힣a-zA-Z\s]{2,10}$/.test(name);
}

function validatePhone(phone) {
  return /^010-\d{4}-\d{4}$/.test(phone);
}