
import { 
    createContext, 
    useContext, 
    useState, 
    useCallback, 
    useMemo 
} from 'react';


// 1. 컨텍스트 생성
export const EmployeeContext = createContext();

// 2. 초기 데이터 (예시)
const initialState = [
  { name: "John", age: 35, job: "frontend", language: "react", pay: 400 },
  { name: "Peter", age: 28, job: "backend", language: "java", pay: 300 },
  { name: "Sue", age: 38, job: "publisher", language: "javascript", pay: 400 },
  { name: "Susan", age: 45, job: "pm", language: "python", pay: 500 },
];

// 3. Provider 컴포넌트
export const EmployeeProvider = ({ children }) => {
  const [infos, setInfos] = useState(initialState);
  const [upInfo, setUpInfo] = useState(null);
  const [mode, setMode] = useState('');
  const [name, setName] = useState('');

  const modes = useMemo(() => ["register", "upgrade", "delete", "초기화"], []);

  const handleSearchName = (n) => {
    setName(n);
    const selected = infos.find(info => info.name === n);
    setUpInfo(selected);
  };

  const handleClick = useCallback((mod) => {
    if (mod === 'delete') {
      if (name) {
        setInfos(prev => prev.filter(item => item.name !== name));
        setName('');
        setMode('');
      } else {
        alert("직원을 선택해 주세요.");
      }
    } else if (mod === '초기화') {
      setInfos(initialState);
      setName('');
      setMode('');
    } else if (mod === 'upgrade') {
      if (name) {
        setMode(mod);
      } else {
        alert("직원을 선택해 주세요.");
      }
    } else {
      setMode(mod);
    }
  }, [name]);

  const handleRegister = (obj) => {
    setInfos(prev => [...prev, obj]);
    setName(obj.name);
    setUpInfo(obj);
    setMode('');
  };

  const handleUpgrade = (obj) => {
    setInfos(prev => prev.map(item => (item.name === obj.name ? obj : item)));
    setMode('');
  };

// 4. Context Value 설정
  const value = {
    infos, upInfo, mode, name, modes,
    handleSearchName, handleClick, handleRegister, handleUpgrade,
    setMode, setName
  };

  return (
    <EmployeeContext.Provider value={value}>
      {children}
    </EmployeeContext.Provider>
  );
};

const useEmployee = () => {
    const context = useContext(EmployeeContext);
    return context;
}

export default useEmployee;


