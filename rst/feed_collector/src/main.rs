use opml::OPML;
use std::fs::File;
use std::io::Read;

fn print_outlines(outlines: &[opml::Outline]) {
    for outline in outlines {
        if let Some(xml_url) = &outline.xml_url {
            println!("RSS Feed: {} - {}", outline.text, xml_url);
        }
        if !outline.outlines.is_empty() {
            print_outlines(&outline.outlines);
        }
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 读取 OPML 文件
    let mut file = File::open("feeds.opml")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    // 解析 OPML 文件
    let opml = OPML::from_str(&contents)?;

    // 打印 OPML 文件的基本信息
    println!("OPML Title: {}", opml.head.unwrap().title.unwrap());

    // 递归提取 RSS 订阅链接
    print_outlines(&opml.body.outlines);

    Ok(())
}
