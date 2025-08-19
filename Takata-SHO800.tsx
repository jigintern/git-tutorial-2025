"use client";
const Home = () => {

    // ロジック部分
    document.querySelectorAll("*").forEach((element) => { // すべてのDOMに対し
        if (element instanceof HTMLElement) {  // 型チェック
            console.log(element.getHTML()) // 要素のHTMLを取得して出力
        }
    })

    return (
        <main>
            hoge
        </main>
    );
}

export default Home;
