import "./Styles.css"
import Result from "../Output/Result";
import ImageInput from "../Input/ImageInput";
function Home()
{
    return(    
    <span className="ReverseImage">
        <p className="Header">Reverse Image</p>
        <ImageInput />
        <Result></Result>
    </span>
    );
}

export default Home;