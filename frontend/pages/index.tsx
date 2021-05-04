import {NextPage} from "next";
import {NavBar} from "../components/navBar";

interface PageProps {
}

const Page: NextPage<PageProps> = () => {
    return (
        <>
            <NavBar/>
            <h1>Homepage</h1>
        </>
    )
}

export default Page;