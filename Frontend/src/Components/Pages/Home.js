import "./Styles.css"
import Result from "../Output/Result";
import ImageInput from "../Input/ImageInput";
function Home()
{
    return(    
    <span className="ReverseImage">
        <h1>Reverse Image</h1>
        <ImageInput />
        <Result></Result>
    </span>
    );
}

export default Home;